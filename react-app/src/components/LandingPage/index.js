import "./LandingPage.css";
import React, { useEffect } from "react";

import Carousel, { CarouselItem } from "../Carousel";
import { useSelector, useDispatch } from "react-redux";
import { allBooks, getAllBooks } from "../../store/books";
import LoadingSpinner from "../LoadingSpinner";
import { allCollections, getAllCollections } from "../../store/collections";
import { useHistory } from "react-router-dom";
import FeaturedGenres from "../FeaturedGenres";

const LandingPage = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const books = useSelector(allBooks);
  const collections = useSelector(allCollections);
  const featuredBooks = collections.filter(
    (collection) => collection.id === 1
  )[0]?.Books;

  useEffect(() => {
    dispatch(getAllBooks());
    dispatch(getAllCollections());
  }, [dispatch]);

  if (!books || !collections) {
    return <LoadingSpinner />;
  }
  return (
    <div className="landing--container">
      <div className="landing-featured-carousel--container">
        <h2 className="landing-featured-carousel--heading">Featured</h2>
        <Carousel className="landing-featured-carousel--component">
          {featuredBooks?.map((book, index) => (
            <CarouselItem
              key={index}
              className="landing-featured-carousel-item--component"
            >
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
      <FeaturedGenres />
    </div>
  );
};

export default LandingPage;
