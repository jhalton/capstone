import "./AdminPortalSidebar.css";
import React from "react";

const AdminPortalSidebar = ({ setCreateCollection, setCreateBook }) => {
  const handleCollectionClick = () => {
    setCreateCollection(true);
    setCreateBook(false);
  };

  const handleBookClick = () => {
    setCreateBook(true);
    setCreateCollection(false);
  };

  const handleViewsClick = () => {
    setCreateBook(false);
    setCreateCollection(false);
  };

  return (
    <div className="admin-portal-sidebar--container">
      <h3>Admin Sidebar component</h3>
      <span onClick={handleViewsClick}>View Collections</span>
      <span onClick={handleCollectionClick}>Create New Collection</span>
      <span onClick={handleBookClick}>Create New Book</span>
    </div>
  );
};

export default AdminPortalSidebar;
