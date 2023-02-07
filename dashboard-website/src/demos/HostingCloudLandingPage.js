import React from "react";
import AnimationRevealPage from "helpers/AnimationRevealPage.js";
import Hero from "components/hero/TwoColumnWithPrimaryBackground.js";
import OurTeam from "components/features/OurTeam";
import MainFeature from "components/features/TwoColWithButton.js";
import Pricing from "components/pricing/ThreePlansWithHalfPrimaryBackground.js";
import Testimonial from "components/testimonials/SimplePrimaryBackground.js";
import FAQ from "components/faqs/TwoColumnPrimaryBackground.js";
import Footer from "components/footers/Footer.js";
import TableauEmbed from "components/TableauEmbed.js";
import serverRedundancyIllustrationImageSrc from "images/server-redundancy-illustration.svg"
import serverSecureIllustrationImageSrc from "images/server-secure-illustration.svg"


export default () => {
  return (
    <AnimationRevealPage>
      <Hero />
      <OurTeam />
      <TableauEmbed />
      {/* <Pricing /> */}
      <MainFeature 
        subheading="Reliable"
        heading="The Importance of Sleep"
        imageSrc={serverRedundancyIllustrationImageSrc}
        buttonRounded={false}
      />
      <MainFeature 
        subheading="Secure"
        heading="What a Good Diet Can Do For You"
        imageSrc={serverSecureIllustrationImageSrc}
        buttonRounded={false}
        textOnLeft={false}
      />
      {/* <Testimonial /> */}
      <FAQ />
      <Footer />
    </AnimationRevealPage>
  );
}
