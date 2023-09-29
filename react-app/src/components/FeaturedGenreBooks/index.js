import "./FeaturedGenreBooks.css";
import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { allCollections } from "../../store/collections";

const FeaturedGenreBooks = ({
  fiction,
  nonfiction,
  horror,
  romance,
  youngAdult,
  scienceFiction,
  autobiography,
}) => {
  const dispatch = useDispatch();
  const collections = useSelector(allCollections);

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
        {selectedFiction.map((book) => (
          <div key={book.id}>
            <span>{book.title}</span>
            <img src={book.frontImage} alt={book.title} />
          </div>
        ))}
      </div>
    );
  }

  if (nonfiction) {
    return (
      <div>
        <h1>Nonfiction</h1>
        {selectedNonfiction.map((book) => (
          <div key={book.id}>
            <span>{book.title}</span>
            <img src={book.frontImage} alt={book.title} />
          </div>
        ))}
      </div>
    );
  }

  if (horror) {
    return (
      <div>
        <h1>Horror</h1>
        {selectedHorror.map((book) => (
          <div key={book.id}>
            <span>{book.title}</span>
            <img src={book.frontImage} alt={book.title} />
          </div>
        ))}
      </div>
    );
  }

  if (romance) {
    return (
      <div>
        <h1>Romance</h1>
        {selectedRomance.map((book) => (
          <div key={book.id}>
            <span>{book.title}</span>
            <img src={book.frontImage} alt={book.title} />
          </div>
        ))}
      </div>
    );
  }

  if (youngAdult) {
    return (
      <div>
        <h1>Young Adult</h1>
        {selectedYoungAdult.map((book) => (
          <div key={book.id}>
            <span>{book.title}</span>
            <img src={book.frontImage} alt={book.title} />
          </div>
        ))}
      </div>
    );
  }

  if (scienceFiction) {
    return (
      <div>
        <h1>Science Fiction</h1>
        {selectedScienceFiction.map((book) => (
          <div key={book.id}>
            <span>{book.title}</span>
            <img src={book.frontImage} alt={book.title} />
          </div>
        ))}
      </div>
    );
  }

  if (autobiography) {
    return (
      <div>
        <h1>Autobiography</h1>
        {selectedAutobiography.map((book) => (
          <div key={book.id}>
            <span>{book.title}</span>
            <img src={book.frontImage} alt={book.title} />
          </div>
        ))}
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
