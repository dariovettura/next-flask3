'use client'
import Image from 'next/image'
import Link from 'next/link'
import { useEffect, useState } from 'react';

export default function Home() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e:any) => {
      e.preventDefault();

      try {
          const res = await fetch('/api/test', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ input }),
          });

          if (!res.ok) {
              throw new Error('Qualcosa è andato storto');
          }

          const data = await res.json();
          setResponse(data.response);
      } catch (error) {
          console.error(error);
          setResponse('Errore nella richiesta');
      }
  };

  return (
      <div>
          <h1>Invia Input</h1>
          <form onSubmit={handleSubmit}>
              <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  placeholder="Scrivi qualcosa..."
                  required
              />
              <button type="submit">Invia</button>
          </form>
          {response && <p>Risposta: {response}</p>}
      </div>
  );
};


