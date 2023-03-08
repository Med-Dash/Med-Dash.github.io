import React from "react";
import AnimationRevealPage from "helpers/AnimationRevealPage.js";
import Hero from "components/hero/TwoColumnWithPrimaryBackground.js";
import OurTeam from "components/features/OurTeam";
import MainFeature from "components/features/TwoColWithButton.js";
import GoodDietFeature from "components/features/GoodDietFeature.js";
import Pricing from "components/pricing/ThreePlansWithHalfPrimaryBackground.js";
import Testimonial from "components/testimonials/SimplePrimaryBackground.js";
import FAQ from "components/faqs/TwoColumnPrimaryBackground.js";
import Footer from "components/footers/Footer.js";
import TableauEmbed from "components/TableauEmbed.js";
import TableauScoresEmbed from "components/TableauScoresEmbed";
import sleepIllustrationImageSrc from "images/sleep.png"
import healthyfoodIllustrationImageSrc from "images/healthyfood.jpg"


export default () => {
  return (
    <AnimationRevealPage>
      <Hero />
      <OurTeam />
      <TableauScoresEmbed/>
      <TableauEmbed />
      {/* <Pricing /> */}
      <MainFeature 
        subheading=""
        heading="The Importance of Sleep"
        imageSrc={sleepIllustrationImageSrc}
        buttonRounded={false}
      />
      <GoodDietFeature 
        subheading=""
        heading="What a Good Diet Can Do For You"
        imageSrc={healthyfoodIllustrationImageSrc}
        buttonRounded={false}
        textOnLeft={false}
      />
      {/* <Testimonial /> */}
      <FAQ />
      <Footer />
    </AnimationRevealPage>
  );
}
