// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import { getFirestore, collection, addDoc, getDocs, query, orderBy, deleteDoc, doc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-firestore.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js";

const firebaseConfig = {
    apiKey: "AIzaSyA5e-82EajWM46uuoua0R2hwAS3O59jgRg",
    authDomain: "agency-6160d.firebaseapp.com",
    projectId: "agency-6160d",
    storageBucket: "agency-6160d.firebasestorage.app",
    messagingSenderId: "163654880838",
    appId: "1:163654880838:web:5fd8f7872ad55cdc504447",
    measurementId: "G-KZ1RNTWE16"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

// Export instances to be used in other scripts
export { db, auth, collection, addDoc, getDocs, query, orderBy, deleteDoc, doc, serverTimestamp };
