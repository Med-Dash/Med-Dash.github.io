import { React } from "react";
import AnimationRevealPage from "helpers/AnimationRevealPage.js";
import Hero from "components/hero/AboutHero.js";
import Features from "components/features/AboutFeatures.js";
import Footer from "components/footers/Footer.js";

const aboutOurProject = () => {
  return (
  <AnimationRevealPage>
    <Hero />
    <Features />
    {/* <Footer /> */}
  </AnimationRevealPage>
  );
}

export default aboutOurProject;
