import "./LandingPage.css";
import React, { useEffect } from "react";

import Carousel, { CarouselItem } from "../Carousel";
import { useSelector, useDispatch } from "react-redux";
import { allBooks, getAllBooks } from "../../store/books";
import LoadingSpinner from "../LoadingSpinner";
import { allCollections, getAllCollections } from "../../store/collections";
import { useHistory } from "react-router-dom";

const LandingPage = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const books = useSelector(allBooks);
  const collections = useSelector(allCollections);
  const featuredBooks = collections.filter(
    (collection) => collection.id === 2
  )[0]?.Books;

  useEffect(() => {
    dispatch(getAllBooks());
    dispatch(getAllCollections());
  }, [dispatch]);

  if (!books || !collections) {
    return <LoadingSpinner />;
  }
  return (
    <div>
      <div className="landing-featured-carousel--container">
        <h2>Featured</h2>
        <Carousel>
          {featuredBooks?.map((book, index) => (
            <CarouselItem key={index}>
              <div>
                <img
                  src={book.frontImage}
                  alt={book.title}
                  className="landing-featured--img"
                  onClick={() => history.push(`/books/${book.id}`)}
                />
              </div>
            </CarouselItem>
          ))}
        </Carousel>
      </div>
    </div>
  );
};

export default LandingPage;
