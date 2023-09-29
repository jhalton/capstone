import "./CollectionDetail.css";
import React, { useEffect } from "react";
import { currentCollection, getCollectionById } from "../../store/collections";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoadingSpinner from "../LoadingSpinner";
import OpenModalButton from "../OpenModalButton";
import AddBookToCollectionModal from "../AddBookToCollectionModal";
import { getAllBooks } from "../../store/books";
import { useModal } from "../../context/Modal";
import DeleteBookFromCollectionModal from "../DeleteBookFromCollectionModal";
import DeleteCollectionModal from "../DeleteCollectionModal";
import EditCollectionModal from "../EditCollectionModal";

const CollectionDetail = () => {
  const dispatch = useDispatch();
  const { collectionId } = useParams();
  const collection = useSelector(currentCollection).Books;
  const collectionInfo = useSelector(currentCollection).Collection;
  const books = useSelector((state) => state.book.allBooks);
  const user = useSelector((state) => state.session.user);
  const history = useHistory();
  const { closeModal } = useModal();

  useEffect(() => {
    dispatch(getCollectionById(collectionId));
    dispatch(getAllBooks());
  }, [dispatch, collectionId, closeModal]);

  if (!collection || !books) {
    return <LoadingSpinner />;
  }

  return (
    <div className="collection-detail--container">
      <h1>{collectionInfo.name}</h1>
      {user?.accountType === "Admin" ? (
        <OpenModalButton
          modalComponent={
            <EditCollectionModal
              collectionId={collectionId}
              collection={collectionInfo}
            />
          }
          buttonText={"Edit"}
        />
      ) : null}
      <p>{collectionInfo.description}</p>
      {user?.accountType === "Admin" ? (
        <div>
          <OpenModalButton
            modalComponent={
              <AddBookToCollectionModal
                collectionId={collectionId}
                books={books}
              />
            }
            buttonText={"Add books"}
          />
          <OpenModalButton
            modalComponent={
              <DeleteCollectionModal collectionId={collectionId} />
            }
            buttonText={"Delete collection"}
          />
        </div>
      ) : null}
      <div className="collection-detail--tile">
        <ul className="collection-detail--ul">
          {collection.map((book) => (
            <li key={book.id} className="collection-detail--li">
              <img
                src={book.frontImage}
                alt={book.title}
                onClick={() => history.push(`/books/${book.id}`)}
              />
              {user?.accountType === "Admin" ? (
                <OpenModalButton
                  modalComponent={
                    <DeleteBookFromCollectionModal
                      book={book}
                      collectionId={collectionId}
                    />
                  }
                  buttonText={
                    <i
                      className="fa-regular fa-trash-can"
                      style={{ color: "#000000" }}
                    ></i>
                  }
                />
              ) : null}
              <span>{book.title}</span>
              <span>
                by {book.authorFirstName} {book.authorLastName}
              </span>
              <div className="collection-detail--stars">
                <div
                  className={
                    book["avgRating"] >= 1
                      ? "collection-detail--rating-filled"
                      : "collection-detail--rating-empty"
                  }
                >
                  <i className="fa-solid fa-star "></i>
                </div>
                <div
                  className={
                    book["avgRating"] >= 1.7
                      ? "collection-detail--rating-filled"
                      : "collection-detail--rating-empty"
                  }
                >
                  <i className="fa-solid fa-star "></i>
                </div>
                <div
                  className={
                    book["avgRating"] >= 2.7
                      ? "collection-detail--rating-filled"
                      : "collection-detail--rating-empty"
                  }
                >
                  <i className="fa-solid fa-star "></i>
                </div>
                <div
                  className={
                    book["avgRating"] >= 3.7
                      ? "collection-detail--rating-filled"
                      : "collection-detail--rating-empty"
                  }
                >
                  <i className="fa-solid fa-star "></i>
                </div>
                <div
                  className={
                    book["avgRating"] >= 4.7
                      ? "collection-detail--rating-filled"
                      : "collection-detail--rating-empty"
                  }
                >
                  <i className="fa-solid fa-star "></i>
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default CollectionDetail;
