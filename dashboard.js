import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";

import { 
getFirestore, doc, setDoc 
} from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

import { 
getAuth, onAuthStateChanged 
} from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";


const firebaseConfig = {
apiKey: "AIzaSyBDPm8SdvGnocloHltybBFsO2XaVpKw_3Y",
authDomain: "autotext-b2e7f.firebaseapp.com",
projectId: "autotext-b2e7f",
storageBucket: "autotext-b2e7f.firebasestorage.app",
messagingSenderId: "51139756433",
appId: "1:51139756433:web:05a60566abaf6993875a30"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

let currentUser = null;

onAuthStateChanged(auth, (user) => {
    if(user){
        currentUser = user;
    } else{
        window.location.href = "login.html";
    }
});

document.getElementById("saveBtn").addEventListener("click", async () => {

    const cities = document.getElementById("cityInput").value.split(",").map(c => c.trim());
    const countries = document.getElementById("countryInput").value.split(",").map(c => c.trim());
    const telegramId = document.getElementById("telegramInput").value;

    if(!currentUser){
        alert("User not logged in");
        return;
    }

    await setDoc(doc(db, "users", currentUser.uid), {
        cities: cities,
        countries: countries,
        telegramId: telegramId,
        createdAt: new Date()

    });

    alert("Preferences saved!");
});
