'use client'
import { useState } from "react";
import { initializeApp } from "firebase/app";
import { getFirestore, collection, addDoc } from "firebase/firestore";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { getStorage, ref, getDownloadURL } from "firebase/storage";

// Configurazione Firebase
const firebaseConfig = {
  apiKey: "AIzaSyCWUMESbBDOk-Z2XMQHYXKA55fdC7uxYOI",
  authDomain: "omega-point-2.firebaseapp.com",
  projectId: "omega-point-2",
  storageBucket: "omega-point-2.appspot.com",
  messagingSenderId: "998952945888",
  appId: "1:998952945888:web:dc4fadd1403e5150092885",
  measurementId: "G-RJ9GGHECP2"
};

// Inizializza Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);
const storage = getStorage(app); // Inizializza Firebase Storage

const UserForm = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    referralcode: "",
    username: "",
  });
  const [serverMessage, setServerMessage] = useState(""); // Stato per i messaggi del server

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      setServerMessage("Iniziando la registrazione...");

      // Autentica l'utente
      const userCredential = await createUserWithEmailAndPassword(
        auth,
        formData.email,
        formData.password
      );
      const user = userCredential.user;

      setServerMessage("Utente registrato con successo!");

      // Salva i dati nella raccolta esistente "UsersData"
      await addDoc(collection(db, "UsersData"), {
        uid: user.uid, // UID dell'utente
        email: formData.email,
        username: formData.username,
        referralcode: formData.referralcode,
      });

      setServerMessage("Dati utente salvati con successo in Firestore!");

      // Ottieni l'URL di download per il file PDF dal Firebase Storage
      const fileRef = ref(storage, "Dieta.pdf"); // Percorso del file
      const url = await getDownloadURL(fileRef);

      setServerMessage("Download URL ottenuto! Il download inizierà automaticamente...");

      // Crea un link temporaneo e attiva il download automatico
      const a = document.createElement("a");
      a.href = url;
      a.download = "Dieta.pdf";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);

      setFormData({ email: "", password: "", referralcode: "", username: "" });
    } catch (error:any) {
      console.error("Error registering user or adding document: ", error);
      setServerMessage(`Errore: ${error.message}`);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-6">User Registration</h1>
      <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 py-6 mb-4 w-full max-w-sm">
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
            Email
          </label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
            Password
          </label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="referralcode">
            Referral Code
          </label>
          <input
            type="text"
            name="referralcode"
            value={formData.referralcode}
            onChange={handleChange}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
            Username
          </label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Submit
        </button>
      </form>

      {/* Mostra i messaggi di stato dal server */}
      {serverMessage && (
        <div className="mt-4 text-center text-gray-700">
          <p>{serverMessage}</p>
        </div>
      )}
    </div>
  );
};

export default UserForm;
