import { React } from "react";
import AnimationRevealPage from "helpers/AnimationRevealPage.js";
import Hero from "components/hero/AboutHero.js";
import Features from "components/features/AboutFeatures.js";

const aboutOurProject = () => {
  return (
  <AnimationRevealPage>
    <Hero />
    <Features />
  </AnimationRevealPage>
  );
}

export default aboutOurProject;
