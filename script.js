import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
// https://firebase.google.com/docs/web/setup#available-libraries
const firebaseConfig = {
  apiKey: "AIzaSyBDPm8SdvGnocloHltybBFsO2XaVpKw_3Y",
  authDomain: "autotext-b2e7f.firebaseapp.com",
  projectId: "autotext-b2e7f",
  storageBucket: "autotext-b2e7f.firebasestorage.app",
  messagingSenderId: "51139756433",
  appId: "1:51139756433:web:05a60566abaf6993875a30",
  measurementId: "G-Y7CDESP4N0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("userEmail").value;
    const password = document.getElementById("userPassword").value;

    try{
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        alert("Logged In!")
        window.location.href = "dashboard.html";
    } catch (error){
        alert("Login Failed!")
    }

});

const signUpForm = document.getElementById("signUpForm");

signUpForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const email = document.getElementById("emailInput").value;
    const password = document.getElementById("passwordInput").value;

    try{
        await createUserWithEmailAndPassword(auth, email, password);
        alert("Account Created!");
    } catch (error){
        alert("Sign Up Failed!" + error.message);
    }
})

