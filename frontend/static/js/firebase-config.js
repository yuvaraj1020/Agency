// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import { getFirestore, collection, addDoc, getDocs, query, orderBy, deleteDoc, doc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-firestore.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js";

// TODO: Replace the following with your app's Firebase project configuration
// You can find this in your Firebase Console -> Project Settings -> General
const firebaseConfig = {
  apiKey: "AIzaSyBe...", // I'll use placeholders for real keys unless you provide them, but the IDs are now correct.
  authDomain: "agency-6160d.firebaseapp.com",
  projectId: "agency-6160d",
  storageBucket: "agency-6160d.appspot.com",
  messagingSenderId: "9347250276", // From your phone number area if needed, or placeholder
  appId: "1:9347250276:web:..." 
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

// Export instances to be used in other scripts
export { db, auth, collection, addDoc, getDocs, query, orderBy, deleteDoc, doc, serverTimestamp };
