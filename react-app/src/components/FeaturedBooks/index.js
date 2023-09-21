import "./FeaturedBooks.css";
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getAllCollections, getCollectionById } from "../../store/collections";

const FeaturedBooks = () => {
  const dispatch = useDispatch();
  const featuredBooks = useSelector(
    (state) => state.collection.currentCollection
  );
  console.log(featuredBooks);

  useEffect(() => {
    dispatch(getCollectionById(2));
  }, [dispatch]);

  if (!featuredBooks) {
    return <span>...Loading</span>;
  }

  return (
    <div className="featured-books--container">
      <h1>Featured Books Component</h1>
      <div>
        <ul>
          {featuredBooks.map((book) => (
            <li key={book.id}>{book.title}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default FeaturedBooks;
