import "./FeaturedGenreBooks.css";
import React from "react";
import { useSelector } from "react-redux";
import { allCollections } from "../../store/collections";
import { useHistory } from "react-router-dom";
import LoadingSpinner from "../LoadingSpinner";

const FeaturedGenreBooks = ({
  fiction,
  nonfiction,
  horror,
  romance,
  youngAdult,
  scienceFiction,
  autobiography,
}) => {
  const collections = useSelector(allCollections);
  const history = useHistory();

  if (!collections) {
    return <LoadingSpinner />;
  }
  //------------------Selected collections----------------------------------
  const selectedFiction = collections.filter(
    (selected) => selected.name === "Fiction"
  )[0].Books;

  const selectedNonfiction = collections.filter(
    (selected) => selected.name === "Nonfiction"
  )[0].Books;

  const selectedHorror = collections.filter(
    (selected) => selected.name === "Horror"
  )[0].Books;

  const selectedRomance = collections.filter(
    (selected) => selected.name === "Romance"
  )[0].Books;

  const selectedYoungAdult = collections.filter(
    (selected) => selected.name === "Young Adult"
  )[0].Books;

  const selectedScienceFiction = collections.filter(
    (selected) => selected.name === "Science Fiction"
  )[0].Books;

  const selectedAutobiography = collections.filter(
    (selected) => selected.name === "Autobiography"
  )[0].Books;

  //------------------------------------------------------------------------

  if (fiction) {
    return (
      <div>
        <h1>Fiction</h1>
        <div className="landing-featured-genre--tile-row">
          {selectedFiction.slice(0, 4).map((book) => (
            <div key={book.id} className="landing-featured-genre--tile">
              <img
                src={book.frontImage}
                alt={book.title}
                className="landing-featured-genre--book"
                onClick={() => history.push(`/books/${book.id}`)}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (nonfiction) {
    return (
      <div>
        <h1>Nonfiction</h1>
        <div className="landing-featured-genre--tile-row">
          {selectedNonfiction.slice(0, 4).map((book) => (
            <div key={book.id} className="landing-featured-genre--tile">
              <img
                src={book.frontImage}
                alt={book.title}
                className="landing-featured-genre--book"
                onClick={() => history.push(`/books/${book.id}`)}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (horror) {
    return (
      <div>
        <h1>Horror</h1>
        <div className="landing-featured-genre--tile-row">
          {selectedHorror.slice(0, 4).map((book) => (
            <div key={book.id} className="landing-featured-genre--tile">
              <img
                src={book.frontImage}
                alt={book.title}
                className="landing-featured-genre--book"
                onClick={() => history.push(`/books/${book.id}`)}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (romance) {
    return (
      <div>
        <h1>Romance</h1>
        <div className="landing-featured-genre--tile-row">
          {selectedRomance.slice(0, 4).map((book) => (
            <div key={book.id} className="landing-featured-genre--tile">
              <img
                src={book.frontImage}
                alt={book.title}
                className="landing-featured-genre--book"
                onClick={() => history.push(`/books/${book.id}`)}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (youngAdult) {
    return (
      <div>
        <h1>Young Adult</h1>
        <div className="landing-featured-genre--tile-row">
          {selectedYoungAdult.slice(0, 4).map((book) => (
            <div key={book.id} className="landing-featured-genre--tile">
              <img
                src={book.frontImage}
                alt={book.title}
                className="landing-featured-genre--book"
                onClick={() => history.push(`/books/${book.id}`)}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (scienceFiction) {
    return (
      <div>
        <h1>Science Fiction</h1>
        <div className="landing-featured-genre--tile-row">
          {selectedScienceFiction.slice(0, 4).map((book) => (
            <div key={book.id} className="landing-featured-genre--tile">
              <img
                src={book.frontImage}
                alt={book.title}
                className="landing-featured-genre--book"
                onClick={() => history.push(`/books/${book.id}`)}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (autobiography) {
    return (
      <div>
        <h1>Autobiography</h1>
        <div className="landing-featured-genre--tile-row">
          {selectedAutobiography.slice(0, 4).map((book) => (
            <div key={book.id} className="landing-featured-genre--tile">
              <img
                src={book.frontImage}
                alt={book.title}
                className="landing-featured-genre--book"
                onClick={() => history.push(`/books/${book.id}`)}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div>
      <h1>Featured Genre Books Component</h1>
    </div>
  );
};

export default FeaturedGenreBooks;
