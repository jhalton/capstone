import "./AdminPortal.css";
import React, { useEffect, useState } from "react";
import AdminPortalSidebar from "../AdminPortalSidebar";
import LoadingSpinner from "../LoadingSpinner";
import { useDispatch, useSelector } from "react-redux";
import { allCollections, getAllCollections } from "../../store/collections";
import CreateBook from "../CreateBook";
import CreateCollection from "../CreateCollection";

const AdminPortal = () => {
  const dispatch = useDispatch();
  const collections = useSelector(allCollections);
  const [createCollection, setCreateCollection] = useState(false);
  const [createBook, setCreateBook] = useState(false);

  useEffect(() => {
    dispatch(getAllCollections());
  }, [dispatch]);

  if (!collections) {
    return <LoadingSpinner />;
  }

  if (createCollection) {
    return (
      <div>
        <AdminPortalSidebar
          collections={collections}
          setCreateCollection={setCreateCollection}
          setCreateBook={setCreateBook}
        />
        <CreateCollection />
      </div>
    );
  }

  if (createBook) {
    return (
      <div>
        <AdminPortalSidebar
          collections={collections}
          setCreateCollection={setCreateCollection}
          setCreateBook={setCreateBook}
        />
        <CreateBook />
      </div>
    );
  }

  return (
    <div className="admin-portal-main--container">
      <h1>Welcome to your Admin Portal</h1>
      <AdminPortalSidebar
        collections={collections}
        setCreateCollection={setCreateCollection}
        setCreateBook={setCreateBook}
      />

      <ul>
        {collections?.map((collection) => (
          <li key={collection.id}>
            <h3>{collection.name}</h3>
            <div className="admin-portal-main--collection-tile">
              {collection.Books
                ? collection.Books?.map((book) => (
                    <div
                      key={book?.id}
                      className="admin-portal-main--collection-tile-book"
                    >
                      <img src={book?.frontImage} alt={book?.title} />
                    </div>
                  ))
                : "This collection doesn't have any books yet"}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AdminPortal;
