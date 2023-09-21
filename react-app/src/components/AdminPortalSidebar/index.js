import "./AdminPortalSidebar.css";
import React from "react";

const AdminPortalSidebar = ({ collections }) => {
  return (
    <div className="admin-portal-sidebar--container">
      <h3>Admin Sidebar component</h3>
      <span>View Collections</span>
      <span>Create New Collection</span>
      <span>Create New Book</span>
    </div>
  );
};

export default AdminPortalSidebar;
