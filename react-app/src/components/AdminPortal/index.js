import "./AdminPortal.css";
import React, { useEffect, useState } from "react";
import AdminPortalSidebar from "../AdminPortalSidebar";
import LoadingSpinner from "../LoadingSpinner";
import { useDispatch, useSelector } from "react-redux";
import { allCollections, getAllCollections } from "../../store/collections";
import { useHistory } from "react-router-dom";
import CreateBook from "../CreateBook";
import CreateCollection from "../CreateCollection";
import { Redirect } from "react-router-dom";

const AdminPortal = () => {
  const dispatch = useDispatch();
  const collections = useSelector(allCollections);
  const history = useHistory();
  const [createCollection, setCreateCollection] = useState(false);
  const [createBook, setCreateBook] = useState(false);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(getAllCollections());
  }, [dispatch]);

  if (!user || user?.accountType !== "Admin") {
    return <Redirect to="/" />;
  }

  if (!collections) {
    return <LoadingSpinner />;
  }

  if (createCollection) {
    return (
      <div className="admin-portal-main--container">
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
      <div className="admin-portal-main--container">
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
      <AdminPortalSidebar
        collections={collections}
        setCreateCollection={setCreateCollection}
        setCreateBook={setCreateBook}
      />
      <div className="admin-portal-main--collections">
        <h1 className="admin-portal-main--collections-header">
          View Collections
        </h1>
        <ul className="admin-portal-main--collections-ul">
          {collections?.map((collection) => (
            <li
              key={collection?.id}
              className="admin-portal-main--collections-li"
            >
              <h3>{collection?.name}</h3>
              <div
                className="admin-portal-main--collection-tile"
                onClick={() => history.push(`/collections/${collection.id}`)}
              >
                {collection?.Books?.length ? (
                  collection?.Books?.slice(0, 4).map((book) => (
                    <div
                      key={book?.id}
                      className="admin-portal-main--collection-tile-book"
                    >
                      <img src={book?.frontImage} alt={book?.title} />
                    </div>
                  ))
                ) : (
                  <div className="admin-portal-main--collection-tile-empty">
                    <p>This collection doesn't have any books</p>
                  </div>
                )}
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AdminPortal;
