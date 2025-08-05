import { useEffect, useState } from 'react';

export default function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/items/')
      .then((res) => res.json())
      .then((data) => setItems(data))
      .catch(() => {
        // ignore errors in this simple demo
      });
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4 text-center">Grooice Demo</h1>
      <div className="max-w-md mx-auto bg-white shadow rounded-lg">
        <ul>
          {items.map((item) => (
            <li
              key={item.id}
              className="flex justify-between px-4 py-2 border-b last:border-b-0"
            >
              <span>{item.name}</span>
              <span className="text-gray-500">{item.category ?? '—'}</span>
            </li>
          ))}
        </ul>
        <div className="p-4 text-right">
          <button className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
            Add Item
          </button>
        </div>
      </div>
    </div>
  );
}
