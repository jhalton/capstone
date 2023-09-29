import "./FeaturedGenres.css";
import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import FeaturedGenreBooks from "../FeaturedGenreBooks";

const FeaturedGenres = () => {
  const history = useHistory();
  const [fiction, setFiction] = useState(false);
  const [nonfiction, setNonfiction] = useState(false);
  const [horror, setHorror] = useState(false);
  const [romance, setRomance] = useState(false);
  const [youngAdult, setYoungAdult] = useState(false);
  const [scienceFiction, setScienceFiction] = useState(false);
  const [autobiography, setAutobiography] = useState(false);

  //----Functions to handle which genre is rendered on the landing page-----
  const handleFiction = () => {
    setFiction(true);
    setNonfiction(false);
    setHorror(false);
    setRomance(false);
    setYoungAdult(false);
    setScienceFiction(false);
    setAutobiography(false);
  };

  const handleNonfiction = () => {
    setFiction(false);
    setNonfiction(true);
    setHorror(false);
    setRomance(false);
    setYoungAdult(false);
    setScienceFiction(false);
    setAutobiography(false);
  };

  const handleHorror = () => {
    setFiction(false);
    setNonfiction(false);
    setHorror(true);
    setRomance(false);
    setYoungAdult(false);
    setScienceFiction(false);
    setAutobiography(false);
  };

  const handleRomance = () => {
    setFiction(false);
    setNonfiction(false);
    setHorror(false);
    setRomance(true);
    setYoungAdult(false);
    setScienceFiction(false);
    setAutobiography(false);
  };

  const handleYoungAdult = () => {
    setFiction(false);
    setNonfiction(false);
    setHorror(false);
    setRomance(false);
    setYoungAdult(true);
    setScienceFiction(false);
    setAutobiography(false);
  };

  const handleScienceFiction = () => {
    setFiction(false);
    setNonfiction(false);
    setHorror(false);
    setRomance(false);
    setYoungAdult(false);
    setScienceFiction(true);
    setAutobiography(false);
  };

  const handleAutobiography = () => {
    setFiction(false);
    setNonfiction(false);
    setHorror(false);
    setRomance(false);
    setYoungAdult(false);
    setScienceFiction(false);
    setAutobiography(true);
  };
  //-----------------------------------------------------------------------

  return (
    <div className="featured-genres--container">
      <h2 className="featured-genres--header">Collections</h2>
      <div className="featured-genres--tiles">
        <div className="featured-genres--fiction featured-genres--type">
          <i
            className="fa-solid fa-book fa-2xl genre-icon"
            onClick={handleFiction}
          ></i>
          <p>Fiction</p>
        </div>
        <div className=" featured-genres--type featured-genres--nonfiction">
          <i
            className="fa-solid fa-monument fa-2xl genre-icon"
            onClick={handleNonfiction}
          ></i>
          <p>Nonfiction</p>
        </div>
        <div className=" featured-genres--type featured-genres--horror">
          <i
            className="fa-solid fa-ghost fa-2xl genre-icon"
            onClick={handleHorror}
          ></i>
          <p>Horror</p>
        </div>
        <div className=" featured-genres--type featured-genres--romance">
          <i
            className="fa-solid fa-face-grin-hearts fa-2xl genre-icon"
            onClick={handleRomance}
          ></i>
          <p>Romance</p>
        </div>
        <div className=" featured-genres--type featured-genres--young-adult">
          <i
            className="fa-solid fa-child-reaching fa-2xl genre-icon"
            onClick={handleYoungAdult}
          ></i>
          <p>Young Adult</p>
        </div>
        <div className=" featured-genres--type featured-genres--science-fiction">
          <i
            className="fa-solid fa-robot fa-2xl genre-icon"
            onClick={handleScienceFiction}
          ></i>
          <p>Science Fiction</p>
        </div>
        <div className=" featured-genres--type featured-genres--autobiography">
          <i
            className="fa-solid fa-person fa-2xl genre-icon"
            onClick={handleAutobiography}
          ></i>
          <p>Autobiography</p>
        </div>
      </div>
      <span
        onClick={() => history.push("/collections")}
        className="featured-genres--browse-link"
      >
        Browse All Collections
      </span>
      <div>
        <FeaturedGenreBooks
          fiction={fiction}
          nonfiction={nonfiction}
          horror={horror}
          romance={romance}
          youngAdult={youngAdult}
          scienceFiction={scienceFiction}
          autobiography={autobiography}
        />
      </div>
    </div>
  );
};

export default FeaturedGenres;
