import "./FeaturedGenres.css";
import React from "react";
import { useHistory } from "react-router-dom";

const FeaturedGenres = () => {
  const history = useHistory();

  return (
    <div className="featured-genres--container">
      <h2 className="featured-genres--header">Collections</h2>
      <div className="featured-genres--tiles">
        <div className="featured-genres--fiction featured-genres--type">
          <i className="fa-solid fa-book fa-2xl genre-icon"></i>
          <p>Fiction</p>
        </div>
        <div className=" featured-genres--type featured-genres--nonfiction">
          <i className="fa-solid fa-monument fa-2xl genre-icon"></i>
          <p>Nonfiction</p>
        </div>
        <div className=" featured-genres--type featured-genres--horror">
          <i className="fa-solid fa-ghost fa-2xl genre-icon"></i>
          <p>Horror</p>
        </div>
        <div className=" featured-genres--type featured-genres--romance">
          <i className="fa-solid fa-face-grin-hearts fa-2xl genre-icon"></i>
          <p>Romance</p>
        </div>
        <div className=" featured-genres--type featured-genres--young-adult">
          <i className="fa-solid fa-child-reaching fa-2xl genre-icon"></i>
          <p>Young Adult</p>
        </div>
        <div className=" featured-genres--type featured-genres--science-fiction">
          <i className="fa-solid fa-robot fa-2xl genre-icon"></i>
          <p>Science Fiction</p>
        </div>
        <div className=" featured-genres--type featured-genres--autobiography">
          <i className="fa-solid fa-person fa-2xl genre-icon"></i>
          <p>Autobiography</p>
        </div>
      </div>
      <span
        onClick={() => history.push("/collections")}
        className="featured-genres--browse-link"
      >
        Browse All Collections
      </span>
    </div>
  );
};

export default FeaturedGenres;
