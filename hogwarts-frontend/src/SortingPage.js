import React from 'react';
import gryffindorImg from './gryfindor.png';
import slytherinImg from './slytherin.png';
import ravenclawImg from './ravenclaw.png';
import hufflepuffImg from './hufflepuff.png';
import './SortingPage.css';

function SortingPage({ house }) {
  let houseImgSrc = '';
  let houseBlurb = '';

  // Determine the appropriate image source and blurb based on the house
  if (house === 'Gryffindor') {
    houseImgSrc = gryffindorImg;
    houseBlurb =
      'Gryffindor, associated with courage and bravery, is aligned with genres like punk, alternative, and rock, as these genres exude boldness and rebellion, resonating with individuals unafraid to stand out and challenge norms.';
  } else if (house === 'Slytherin') {
    houseImgSrc = slytherinImg;
    houseBlurb =
      'Slytherin, known for ambition and resourcefulness, is associated with rap, hip hop, and metal genres. These genres attract individuals with a strong drive for success and a willingness to embrace darker, edgier elements, aligning with Slytherin\'s cunning nature.';
  } else if (house === 'Ravenclaw') {
    houseImgSrc = ravenclawImg;
    houseBlurb =
      'Ravenclaw, emphasizing intelligence and creativity, is linked to classical, jazz, and ambient genres. These genres attract those with a deep appreciation for intricate sounds and innovative musical styles, mirroring the intellectual curiosity of Ravenclaw members.';
  } else if (house === 'Hufflepuff') {
    houseImgSrc = hufflepuffImg;
    houseBlurb =
      'Hufflepuff, valuing loyalty and kindness, corresponds to acoustic, country, and pop genres, reflecting a warm and friendly nature. These genres attract individuals who prioritize harmony and connection, traits emblematic of Hufflepuff.';
  }

  return (
    <div className="SortingPage">
      <h1>You have been sorted into {house}!</h1>
      <img src={houseImgSrc} alt={house} className="house-image" />
      <p>{houseBlurb}</p>
    </div>
  );
}

export default SortingPage;
