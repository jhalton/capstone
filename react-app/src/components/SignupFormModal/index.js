import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";
import LoginFormModal from "../LoginFormModal";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [street_address, setStreetAddress] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [account_type, setAccountType] = useState("Consumer");
  const [membership, setMembership] = useState(false);
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal, setModalContent } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password === confirmPassword) {
      const data = await dispatch(
        signUp(
          first_name,
          last_name,
          email,
          phone,
          street_address,
          city,
          state,
          account_type,
          membership,
          password
        )
      );
      if (data?.errors) {
        setErrors(data?.errors);
      } else {
        closeModal();
      }
    } else {
      setErrors({
        password:
          "Confirm Password field must be the same as the Password field",
      });
    }
  };

  return (
    <>
      <h1 className="sign-up--modal-header">Sign Up</h1>

      <form className="sign-up--modal" onSubmit={handleSubmit}>
        <label>
          First name
          <input
            type="text"
            value={first_name}
            onChange={(e) => setFirstName(e.target.value)}
          />
        </label>
        {errors.first_name && <p className="errors">{errors.first_name}</p>}
        <label>
          Last name
          <input
            type="text"
            value={last_name}
            onChange={(e) => setLastName(e.target.value)}
          />
        </label>
        {errors.last_name && <p className="errors">{errors.last_name}</p>}
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            // required
          />
        </label>
        {errors.email && <p className="errors">{errors.email}</p>}
        <label>
          Phone
          <input
            type="text"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </label>
        {errors.phone && <p className="errors">{errors.phone}</p>}
        <label>
          Street address
          <input
            type="text"
            value={street_address}
            onChange={(e) => setStreetAddress(e.target.value)}
          />
        </label>
        {errors.street_address && (
          <p className="errors">{errors.street_address}</p>
        )}
        <label>
          City
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
          />
        </label>
        {errors.city && <p className="errors">{errors.city}</p>}
        <label>
          State
          <input
            type="text"
            value={state}
            onChange={(e) => setState(e.target.value)}
          />
        </label>
        {errors.state && <p className="errors">{errors.state}</p>}
        <label className="sign-up--modal-accounttype">
          Account Type
          <select onChange={(e) => setAccountType(e.target.value)}>
            <option value={account_type}>Consumer</option>
          </select>
        </label>
        {errors.account_type && <p className="errors">{errors.account_type}</p>}
        <label>
          Membership
          <select
            value={membership}
            onChange={(e) => setMembership(e.target.value)}
          >
            <option value={true}>Yes</option>
            <option value={false}>No</option>
          </select>
        </label>
        {errors.membership && <p className="errors">{errors.membership}</p>}
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            // required
          />
        </label>
        {errors.password && <p className="errors">{errors.password}</p>}
        <label>
          Confirm Password
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            // required
          />
        </label>
        <button type="submit">Sign Up</button>
        <span className="sign-up-modal--existing-user">
          <span>Already have an account?</span>{" "}
          <span
            className="sign-up-modal--existing-user-login"
            onClick={() => setModalContent(<LoginFormModal />)}
          >
            Log in
          </span>
        </span>
      </form>
    </>
  );
}

export default SignupFormModal;
