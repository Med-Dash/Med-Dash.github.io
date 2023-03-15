import React from "react";
import GlobalStyles from 'styles/GlobalStyles';
import { css } from "styled-components/macro"; //eslint-disable-line

import MainLandingPage from "demos/LandingPage.js";
import ThankYouPage from "ThankYouPage.js";

import { HashRouter as Router, Routes, Route } from "react-router-dom";

import AboutOurProject from "demos/AboutOurProject.js";

export default function App() {
  // If you want to disable the animation just use the disabled `prop` like below on your page's component
  // return <AnimationRevealPage disabled>xxxxxxxxxx</AnimationRevealPage>;


  return (
    <>
      <GlobalStyles />
      <Router>
        <Routes>
          <Route path="/thank-you" element={<ThankYouPage />} />
          <Route path="/" element={<MainLandingPage />} />
          <Route path="/About-Our-Project" element={<AboutOurProject />} />
        </Routes>
      </Router>
    </>
  );
}