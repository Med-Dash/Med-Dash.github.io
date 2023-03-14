import React from "react";
import tw from "twin.macro";
import { css } from "styled-components/macro"; //eslint-disable-line
import HeaderBase, {
  LogoLink as LogoLinkBase,
  NavLinks,
  NavLink as NavLinkBase,
  PrimaryLink as PrimaryLinkBase
} from "../headers/light.js";
import { Container as ContainerBase, ContentWithVerticalPadding, Content2Xl } from "components/misc/Layouts.js";
import { SectionHeading } from "components/misc/Headings.js";
import { SectionDescription } from "components/misc/Typography.js";
import { PrimaryButton as PrimaryButtonBase } from "components/misc/Buttons.js";
import logoImageSrc from "images/dashboard_icon.svg";
import dashboardImage from "images/dashboard-growth.png";
import AboutOurProject from "demos/AboutOurProject.js";

const PrimaryBackgroundContainer = tw.div`-mx-8 px-8 bg-primary-800 text-gray-100`;
const Header = tw(HeaderBase)`max-w-none -mt-8 py-8 -mx-8 px-8`;
const NavLink = tw(NavLinkBase)`lg:text-gray-100 lg:hocus:text-gray-300 lg:hocus:border-gray-100`;
const LogoLink = tw(LogoLinkBase)`text-gray-100 hocus:text-gray-300`;
const PrimaryLink = tw(PrimaryLinkBase)`shadow-raised lg:bg-primary-400 lg:hocus:bg-primary-500`;

const Container = tw(ContainerBase)``;
const Row = tw.div`flex items-center flex-col lg:flex-row`;
const Column = tw.div`lg:w-1/2`;
const TextColumn = tw.div`text-center lg:text-left`;
const IllustrationColumn = tw(Column)`mt-16 lg:mt-0 lg:ml-16`;
const Heading = tw(SectionHeading)`max-w-3xl lg:max-w-4xl lg:text-left leading-tight`;
const Description = tw(SectionDescription)`mt-4 max-w-2xl text-gray-100 lg:text-base mx-auto lg:mx-0`;
const PrimaryButton = tw(PrimaryButtonBase)`mt-8 text-sm sm:text-base px-6 py-5 sm:px-10 sm:py-5 bg-primary-400 inline-block hocus:bg-primary-500`;
const Image = tw.img`w-144 ml-auto`

const Hero = ({ 
  ourTeamRef, 
  dashboardRef,
  heading = "MedDash",
  description = "MedDash aims to consolidate multiple sources of health data into a comprehensive medical dashboard",
  primaryButtonText = "Explore MedDash Below!",
  imageSrc = dashboardImage, 
  }) => {
    const logoLink = (
      <LogoLink href="/">
        <img src={logoImageSrc} alt="Logo" />
        MedDash
      </LogoLink>
    );
    const navLinks = [
      <NavLinks key={1}>
        <NavLink  onClick={() => ourTeamRef.current.scrollIntoView({ behavior: "smooth" })} >Our Team</NavLink>
        <NavLink onClick={() => dashboardRef.current.scrollIntoView({ behavior: "smooth" })} >Dashboard</NavLink>
        <NavLink href="/#/About-Our-Project">About our Project</NavLink>
      </NavLinks>
    ];
    return (
      <PrimaryBackgroundContainer>
        <Content2Xl>
          <Header logoLink={logoLink} links={navLinks} />
          <Container>
            <ContentWithVerticalPadding>
              <Row>
                <TextColumn>
                  <Heading>{heading}</Heading>
                  <Description>{description}</Description>
                  <PrimaryButton as="a" onClick={() => dashboardRef.current.scrollIntoView({ behavior: "smooth" })} >{primaryButtonText}</PrimaryButton>
                </TextColumn>
                <IllustrationColumn>
                  <Image src={imageSrc} />
                </IllustrationColumn>
              </Row>
            </ContentWithVerticalPadding>
          </Container>
        </Content2Xl>
      </PrimaryBackgroundContainer>
    );
  };

export default Hero;
