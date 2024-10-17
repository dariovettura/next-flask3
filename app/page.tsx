'use client'
import { useState } from 'react';



export default function Home() {


  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
    <h1 className="text-3xl font-bold mb-6">Invia Input</h1>
    <form onSubmit={()=>(console.log(''))} className="bg-white shadow-md rounded px-8 py-6 mb-4">
     
    </form>
    {/* {response && <div className="bg-gray-200 p-4 rounded">{response}</div>}  */}
</div>
  );
};
