import "./BrowseCollections.css";
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { allCollections, getAllCollections } from "../../store/collections";
import LoadingSpinner from "../LoadingSpinner";
import { useHistory } from "react-router-dom";

const BrowseCollections = () => {
  const collections = useSelector(allCollections);
  const dispatch = useDispatch();
  const history = useHistory();

  useEffect(() => {
    dispatch(getAllCollections());
  }, [dispatch]);

  if (!collections) {
    return <LoadingSpinner />;
  }

  return (
    <div className="browse-collections--container">
      <h1>Browse Collections</h1>
      <ul className="browse-collections--ul">
        {collections?.map((collection) => (
          <li key={collection.id} className="browse-collections--li">
            <h3>{collection.name}</h3>
            <div
              className="browse-collections--tile"
              onClick={() => history.push(`/collections/${collection.id}`)}
            >
              {collection.Books.length ? (
                collection.Books?.slice(0, 4).map((book) => (
                  <div key={book.id} className="browse-collections--tile-book">
                    <img src={book?.frontImage} alt={book?.title} />
                  </div>
                ))
              ) : (
                <div className="browse-collections--tile-empty">
                  <p>
                    It looks like this collection doesn't have any books yet!
                  </p>
                </div>
              )}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BrowseCollections;
