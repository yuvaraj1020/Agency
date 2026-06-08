from flask import Blueprint, session, jsonify, request
from models.database import get_db

admin_bp = Blueprint('admin', __name__)

def require_admin():
    if 'agent_id' not in session:
        return jsonify({'error': 'Unauthorized', 'authenticated': False}), 401
    return None

@admin_bp.route('/api/stats')
def stats():
    err = require_admin()
    if err: return err
    conn = get_db()
    leads_count = conn.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
    new_leads = conn.execute("SELECT COUNT(*) FROM leads WHERE status='New'").fetchone()[0]
    users_count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    conn.close()
    return jsonify({
        'success': True,
        'stats': {
            'total_leads': leads_count,
            'new_leads': new_leads,
            'total_users': users_count
        }
    })

@admin_bp.route('/api/agents')
def get_agents():
    err = require_admin()
    if err: return err
    conn = get_db()
    agents = conn.execute("SELECT id, name, email, role, created_at FROM agents ORDER BY created_at DESC").fetchall()
    conn.close()
    return jsonify({'success': True, 'agents': [dict(a) for a in agents]})
