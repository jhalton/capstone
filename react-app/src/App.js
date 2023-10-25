import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import LandingPage from "./components/LandingPage";
import CollectionDetail from "./components/CollectionDetail";
import BrowseCollections from "./components/BrowseCollections";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import AdminPortal from "./components/AdminPortal";
import BookDetail from "./components/BookDetail";
import WishlistDetail from "./components/WishlistDetail";
import ViewWishlists from "./components/ViewWishlists";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login">
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route exact path="/">
            <LandingPage />
          </Route>
          <Route path="/collections/:collectionId">
            <CollectionDetail />
          </Route>
          <Route exact path="/collections">
            <BrowseCollections />
          </Route>
          <ProtectedRoute path="/admin-portal">
            <AdminPortal />
          </ProtectedRoute>
          <Route path="/books/:bookId">
            <BookDetail />
          </Route>
          <Route path="/wishlists/all">
            <ViewWishlists />
          </Route>
          <Route path="/wishlists/:wishlistId">
            <WishlistDetail />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
