'use client'
import { useState } from 'react';



export default function Home() {
  const [checkin, setCheckin] = useState('');
  const [checkout, setCheckout] = useState('');
  const [pax, setPax] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e: any) => {
      e.preventDefault();

      // Costruisci il link utilizzando i parametri forniti
      const link = `https://book.octorate.com/octobook/site/reservation/result.xhtml?checkin=${checkin}&checkout=${checkout}&pax=${pax}`;

      try {
          const res = await fetch('/api/test', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ link }), // Passa il link costruito
          });

          if (!res.ok) {
              throw new Error('Qualcosa è andato storto');
          }

          const data = await res.json();
          setResponse(JSON.stringify(data.rooms, null, 2));
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
                  type="date"
                  value={checkin}
                  onChange={(e) => setCheckin(e.target.value)}
                  placeholder="Check-in"
                  required
              />
              <input
                  type="date"
                  value={checkout}
                  onChange={(e) => setCheckout(e.target.value)}
                  placeholder="Check-out"
                  required
              />
              <input
                  type="number"
                  value={pax}
                  onChange={(e) => setPax(e.target.value)}
                  placeholder="Numero di persone"
                  required
              />
              <button type="submit">Invia</button>
          </form>
          {response && <pre>Risposta: {response}</pre>} {/* Usando <pre> per formattazione */}
      </div>
  );
};
