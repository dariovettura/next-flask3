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
              body: JSON.stringify({ checkin,checkout,pax }), // Passa il link costruito
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
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
    <h1 className="text-3xl font-bold mb-6">Invia Input</h1>
    <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 py-6 mb-4">
        <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="checkin">
                Check-in
            </label>
            <input
                type="date"
                value={checkin}
                onChange={(e) => setCheckin(e.target.value)}
                required
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
        </div>
        <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="checkout">
                Check-out
            </label>
            <input
                type="date"
                value={checkout}
                onChange={(e) => setCheckout(e.target.value)}
                required
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
        </div>
        <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="pax">
                Numero di persone
            </label>
            <input
                type="number"
                value={pax}
                onChange={(e) => setPax(e.target.value)}
                required
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
        </div>
        <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
        >
            Invia
        </button>
    </form>
    {response && <pre className="bg-gray-200 p-4 rounded">{response}</pre>} {/* Usando <pre> per formattazione */}
</div>
  );
};
