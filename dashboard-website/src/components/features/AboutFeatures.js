import React from "react";
import styled from "styled-components";
import tw from "twin.macro";
import { ReactComponent as SvgDotPatternIcon } from "../../images/dot-pattern.svg";
import { SectionHeading as HeadingTitle } from "../misc/Headings.js";

const Container = tw.div`relative`;

const SingleColumn = tw.div`max-w-screen-xl mx-auto py-20 lg:py-24`;

const HeadingInfoContainer = tw.div`flex flex-col items-center`;
const HeadingDescription = tw.p`mt-4 font-medium text-gray-600 text-center max-w-sm`;

const Content = tw.div`mt-16`;

const Card = styled.div(props => [
  tw`mt-24 md:flex justify-center items-center`,
  props.reversed ? tw`flex-row-reverse` : "flex-row"
]);
const Image = styled.div(props => [
  `background-image: url("${props.imageSrc}");`,
  tw`rounded md:w-1/2 lg:w-5/12 xl:w-1/3 flex-shrink-0 h-80 md:h-144 bg-cover bg-center mx-4 sm:mx-8 md:mx-4 lg:mx-8`
]);
const Details = tw.div`mt-4 md:mt-0 md:max-w-md mx-4 sm:mx-8 md:mx-4 lg:mx-8`;
const Subtitle = tw.div`font-bold tracking-wide text-secondary-100`;
const Title = tw.h4`text-3xl font-bold text-gray-900`;
const Description = tw.p`mt-2 text-sm leading-loose`;
const Link = tw.a`inline-block mt-4 text-sm text-primary-500 font-bold cursor-pointer transition duration-300 border-b-2 border-transparent hover:border-primary-500`;

const SvgDotPattern1 = tw(
  SvgDotPatternIcon
)`absolute top-0 left-0 transform -translate-x-20 rotate-90 translate-y-8 -z-10 opacity-25 text-primary-500 fill-current w-24`;
const SvgDotPattern2 = tw(
  SvgDotPatternIcon
)`absolute top-0 right-0 transform translate-x-20 rotate-45 translate-y-24 -z-10 opacity-25 text-primary-500 fill-current w-24`;
const SvgDotPattern3 = tw(
  SvgDotPatternIcon
)`absolute bottom-0 left-0 transform -translate-x-20 rotate-45 -translate-y-8 -z-10 opacity-25 text-primary-500 fill-current w-24`;
const SvgDotPattern4 = tw(
  SvgDotPatternIcon
)`absolute bottom-0 right-0 transform translate-x-20 rotate-90 -translate-y-24 -z-10 opacity-25 text-primary-500 fill-current w-24`;

export default () => {
  const cards = [
    {
      imageSrc:
        "https://drive.google.com/uc?export=view&id=1_K39xSShjSusPD0QO2Md0XLJPOI0nC9j",
      title: "Introduction",
      description:
        "As health sensor technology becomes more advanced and common amongst the general population, we as data scientists are provided with a whole plethora of health related data that can provide meaningful insights to a person's health status. Our project aims to combine all the different forms of sensor data into a consolidated dashboard that will provide the user with a snapshot of their current health status."
    },

    {
      imageSrc:
        "https://drive.google.com/uc?export=view&id=1zr43cNUJ_Gmchos0jvujhUqWAmlg9B06",
      title: "Background",
      description:
        "Major insufficiencies in healthcare systems today leave patients and clinicians alike wanting for a more effective way of receiving and giving care. Several major deficiencies are 1) the lack of an integrated Electronic Health Record (EHR), lifelog, and personal omics data, and 2) the lack of standardization across healthcare systems, data standards, and terminologies. This incompatibility creates inefficiencies in operating personalized medicine, leading to problems with interoperability and introducing ambiguity into the healthcare environment, especially amongst patients, their providers, and organizations. We talked to real patients who have struggled with these issues in their medical are history, and identified the core problems they were having with the way care was prescribed to them. Using this information, we proceeded to come up with a solution that could help boost the communication and understanding between patients and their healthcare providers.",
    },

    {
      imageSrc:
        "https://drive.google.com/uc?export=view&id=1cTbxtdjDHmY3yTnR1rrP019hAL0DuAGz",
      title: "Data Collection",
      description:
        "We were given data from volunteer patients that were eager to help with our project. The data comes from the Oura Ring API and includes variables such as: heart rate, calories burned, number of steps, etc. This is unique from other dashboards as we are obtaining the data from the patients themselves that they provide from different sources",
    },
    {
      imageSrc:
        "https://drive.google.com/uc?export=view&id=1bGF6Jhc8zjGdHE-PdjfRtHTe90KubK8A",
      title: "Methods",
      description:
        "We used Tableau as the primary tool to integrate visualizations onto our website while using Pandas and Numpy to create a pipeline that is designed to pull, read, clean, standardize, and add features to the data given to our team from the Oura Ring Apple Health APIs. To host our work, we used React.js hosted on Github Pages  to create a website that would allow the user to interact with the visualizations. We also leveraged Sci-kit learn to incorporate predictive analytics in regards to determining if a reading was taken on a weekday or weekend.",
    }
  ];

  return (
    <Container>
      <SingleColumn>
        <HeadingInfoContainer>
          {/* <HeadingTitle>Popular Events</HeadingTitle> */}
          <HeadingDescription>
            The purpose and methodology behind our integrative medical dashboard
          </HeadingDescription>
        </HeadingInfoContainer>

        <Content>
          {cards.map((card, i) => (
            <Card key={i} reversed={i % 2 === 1}>
              <Image imageSrc={card.imageSrc} />
              <Details>
                <Subtitle>{card.subtitle}</Subtitle>
                <Title>{card.title}</Title>
                <Description>{card.description}</Description>
              </Details>
            </Card>
          ))}
        </Content>
      </SingleColumn>
      <SvgDotPattern1 />
      <SvgDotPattern2 />
      <SvgDotPattern3 />
      <SvgDotPattern4 />
    </Container>
  );
};
