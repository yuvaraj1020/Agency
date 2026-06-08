#!/usr/bin/env python3
"""
Digital Marketing Agency - Frontend Development Server
Serves static files and proxies API requests to backend
"""

import http.server
import socketserver
import urllib.request
import urllib.error
import urllib.parse
import sys
import os
import json
from urllib.parse import urlparse, parse_qs
from pathlib import Path

PORT = int(os.getenv('PORT', 8000))
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:5000')

class DMAProxyHandler(http.server.SimpleHTTPRequestHandler):
    """Handle HTTP requests with proxy support for API routes"""
    
    def log_message(self, format, *args):
        """Override logging to show request details"""
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.client_address[0]:15} - {format%args}\n")
    
    def proxy_request(self):
        """Proxy request to backend server"""
        url = BACKEND_URL + self.path
        
        # Read request body if present
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else None
        
        # Filter and forward headers
        headers = {}
        excluded_headers = ['host', 'connection', 'content-length', 'accept-encoding', 'transfer-encoding']
        for k, v in self.headers.items():
            if k.lower() not in excluded_headers:
                headers[k] = v
        
        if body:
            headers['Content-Length'] = str(len(body))
        
        # Add CORS headers
        headers['Origin'] = f'http://localhost:{PORT}'
        
        try:
            # Create and send request
            req = urllib.request.Request(url, data=body, headers=headers, method=self.command)
            with urllib.request.urlopen(req, timeout=30) as response:
                self.send_response(response.status)
                
                # Forward response headers
                for k, v in response.headers.items():
                    if k.lower() not in excluded_headers:
                        self.send_header(k, v)
                
                # Add CORS headers to response
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
                
                self.end_headers()
                self.wfile.write(response.read())
                
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            for k, v in e.headers.items():
                if k.lower() not in excluded_headers:
                    self.send_header(k, v)
            
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            try:
                self.wfile.write(e.read())
            except:
                pass
                
        except Exception as e:
            self.send_response(502)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            error_response = {
                'error': 'Bad Gateway',
                'message': str(e),
                'backend_url': BACKEND_URL
            }
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Content-Length', '0')
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        if self._should_proxy():
            return self.proxy_request()
        return super().do_GET()
    
    def do_POST(self):
        """Handle POST requests"""
        return self.proxy_request()
    
    def do_PUT(self):
        """Handle PUT requests"""
        return self.proxy_request()
    
    def do_DELETE(self):
        """Handle DELETE requests"""
        return self.proxy_request()
    
    def do_PATCH(self):
        """Handle PATCH requests"""
        return self.proxy_request()
    
    def _should_proxy(self):
        """Determine if request should be proxied to backend"""
        api_prefixes = ['/api/', '/auth/', '/admin/', '/leads', '/contact']
        return any(self.path.startswith(prefix) for prefix in api_prefixes)
    
    def translate_path(self, path):
        """Override to serve from current directory"""
        # Remove query string
        path = path.split('?')[0]
        
        # Serve index.html for root
        if path == '/' or path == '':
            path = '/index.html'
        
        # Convert to file path
        return super().translate_path(path)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Threaded TCP server to handle multiple requests"""
    allow_reuse_address = True
    daemon_threads = True


def main():
    """Start the development server"""
    print("\n" + "="*60)
    print("Digital Marketing Agency - Frontend Dev Server")
    print("="*60)
    print(f"\nServer:  http://localhost:{PORT}")
    print(f"Backend: {BACKEND_URL}")
    print("\nServing static files from current directory")
    print("Proxying API requests to backend:\n")
    print("  • /api/*      -> Backend API")
    print("  • /auth/*     -> Authentication")
    print("  • /admin/*    -> Admin API")
    print("  • /leads/*    -> Leads API")
    print("  • /contact/*  -> Contact API")
    print("\n" + "="*60)
    print("Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    try:
        with ThreadedTCPServer(("", PORT), DMAProxyHandler) as httpd:
            print(f"[OK] Server started successfully at http://localhost:{PORT}\n")
            httpd.serve_forever()
    except OSError as e:
        print(f"\n[ERROR] Failed to start server: {e}")
        print(f"Port {PORT} might be already in use.")
        print(f"Try running: netstat -ano | findstr :{PORT}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n[OK] Shutting down gracefully...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
