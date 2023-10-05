import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data?.errors) {
      setErrors(data?.errors);
    } else {
      closeModal();
    }
  };

  const handleDemoAdminLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("admin@aa.io", "password"));
    if (data?.errors) {
      setErrors(data.errors);
    } else {
      closeModal();
    }
  };

  const handleDemoConsumerLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("demo@aa.io", "password"));
    if (data?.errors) {
      setErrors(data.errors);
    } else {
      closeModal();
    }
  };

  return (
    <div className="login-modal--container">
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        {errors.email && <p className="errors">{errors.email}</p>}
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {errors.password && <p className="errors">{errors.password}</p>}

        <button type="submit">Log In</button>
      </form>
      <div className="login-modal--demo">
        <span onClick={handleDemoConsumerLogin}>Demo Consumer</span>|
        <span onClick={handleDemoAdminLogin}>Demo Admin</span>
      </div>
    </div>
  );
}

export default LoginFormModal;
