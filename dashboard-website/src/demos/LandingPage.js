import { React, useRef }  from "react";
import AnimationRevealPage from "helpers/AnimationRevealPage.js";
import Hero from "components/hero/TwoColumnWithPrimaryBackground.js";
import OurTeam from "components/features/OurTeam";
import MainFeature from "components/features/TwoColWithButton.js";
import GoodDietFeature from "components/features/GoodDietFeature.js";
import FAQ from "components/faqs/TwoColumnPrimaryBackground.js";
import Footer from "components/footers/Footer.js";
import TableauEmbed from "components/TableauEmbed.js";
import TableauScoresEmbed from "components/TableauScoresEmbed";
import sleepIllustrationImageSrc from "images/sleep.png"
import healthyfoodIllustrationImageSrc from "images/healthyfood.jpg"


export default () => {
  const ourTeamRef = useRef(null);
  const dashboardRef = useRef(null);
  return (
    <AnimationRevealPage>
      <Hero ourTeamRef={ourTeamRef} dashboardRef={dashboardRef}/>
      <OurTeam  ref={ourTeamRef}/>
      <TableauScoresEmbed ref={dashboardRef}/>
      <TableauEmbed />
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
