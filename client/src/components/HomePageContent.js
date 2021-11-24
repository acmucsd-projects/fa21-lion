import React from "react";
import {Container, Row, Col, Button, Image} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import styled from "styled-components";

const HomePageContainer = styled(Container)`
    min-height: 65vh;
    padding: 48px;
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: calc(10px + 2vmin);
    color: Gray;
`;

const Frame4 = styled(Col)`
    flex-direction: column;
    align-items: flex-start;
    position: static;
    margin: 16px 0px;
`;

const TryNowButtonDiv = styled(Row)`
    display: flex;
    flex-direction: row;
    position: static;
    flex: none;
    flex-grow: 0;
    margin: 16px 0px;
`;

const TryNowButton = styled(Button)`
    background-color: MediumTurquoise;
    border: none;
    position: static;
    flex: none;
    flex-grow: 0;
    margin: 16px 0px;
    max-width: 120px;
`;

const HomePageImage = styled(Image)`
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-shrink: 0;
    min-width: 100%;
    min-height: 100%;
`;

function HomePageContent(props) {

	return (
		<HomePageContainer>
            <Row>
				<Frame4 xs={12} sm={6} md={6}>
					<h1 style={{'text-align':'left'}}>
                        Lorem Ipsum
					</h1>
					<h3 style={{'text-align':'left'}}>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
                        ut labore et dolore magna aliqua.
					</h3>
                    <TryNowButtonDiv class="text-left">
                        <TryNowButton>Try Now</TryNowButton>
                    </TryNowButtonDiv>
				</Frame4>
                <Col className="center">
					<HomePageImage
                        src="https://images.unsplash.com/photo-1585468274952-66591eb14165?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8N3x8fGVufDB8fHx8&w=1000&q=80"
						fluid
					/>
				</Col>
			</Row>
		</HomePageContainer>
	);
}

export default HomePageContent;