import React from "react";
import AnimationRevealPage from "helpers/AnimationRevealPage.js";
import Hero from "components/hero/AboutHero.js";
import Features from "components/features/AboutFeatures.js";
import Blog from "components/blogs/AboutBlog.js";
import Testimonial from "components/testimonials/AboutTestimonial";
import Footer from "components/footers/Footer.js";

export default () => (
  <AnimationRevealPage>
    <Hero />
    <Features />
    <Footer />
  </AnimationRevealPage>
);
