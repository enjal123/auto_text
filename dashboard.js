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


function showAlert(message) {
        const alertBox = document.getElementById('customAlert');
        const alertMessage = document.getElementById('alertMessage')

        alertMessage.textContent = message;
        alertBox.classList.remove('hidden');

        setTimeout(() => {
            alertBox.classList.add('hidden');
        }, 3000);

    }

loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("userEmail").value;
    const password = document.getElementById("userPassword").value;

    if(!email || !password){
        showAlert("Please fill out all fields before saving!")
        return;
    }
    try{
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        showAlert("Logged In!")
        setTimeout(() =>{
            window.location.href = "dashboard.html";
        }, 1500);
        
    } catch (error){
        showAlert("Login Failed!")
    }

});

const signUpForm = document.getElementById("signUpForm");

signUpForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const email = document.getElementById("emailInput").value;
    const password = document.getElementById("passwordInput").value;

    try{
        await createUserWithEmailAndPassword(auth, email, password);
        showAlert("Account Created!");
    } catch (error){
        showAlert("Sign Up Failed!" + error.message);
    }
})

