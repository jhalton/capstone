import "./FeaturedBooks.css";
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { currentCollection, getCollectionById } from "../../store/collections";

const FeaturedBooks = () => {
  const dispatch = useDispatch();
  const featured = useSelector(currentCollection);
  const featuredBooks = featured.Books;

  //Gets the Featured Books, which are collectionId 2.
  useEffect(() => {
    dispatch(getCollectionById(2));
  }, [dispatch]);

  if (!featuredBooks) {
    return <span>...Loading</span>;
  }

  return (
    <div className="featured-books--container">
      <h3>Featured</h3>
      <div>
        <ul>
          {featuredBooks?.map((book) => (
            <li key={book.id}>
              <img src={book.frontImage} alt={book.title} />
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default FeaturedBooks;
