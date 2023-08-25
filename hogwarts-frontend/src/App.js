import React, { useEffect, useState } from 'react';
import HogwartsCrestImage from './NicePng_hogwarts-crest-png_1467334.png';
import SortingPage from './SortingPage';
import './App.css';

function App() {
  const [house, setHouse] = useState('');
  const [showSortingPage, setShowSortingPage] = useState(false);
  useEffect(() => {
    async function fetchHouse() {
      try {
        const response = await fetch('http://localhost:8000/hogwarts_house/'); 
        const data = await response.json();
        console.log(data); // Add this line to see the fetched data in the browser console
        setHouse(data.house);
      } catch (error) {
        console.error("Error fetching Hogwarts house:", error);
      }
    }
    fetchHouse();
  }, []);

  const handleSortButtonClick = () => {
    setShowSortingPage(true);
  };

  return (
    <div className="App">
      <header className="App-header">
        {showSortingPage ? (
          <SortingPage house={house} />
        ) : (
          <>
            <h1>Spotify Hogwarts House</h1>
            <button onClick={handleSortButtonClick} className="sort-button"> 
            Sort Me!
            </button>
            <img src={HogwartsCrestImage} alt="Hogwarts Crest" className="hogwarts-crest-image" />
          </>
        )}
      </header>
    </div>
  );
}

export default App;
