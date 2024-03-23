import React, { useEffect, useState } from 'react';
import { Col, Row, Container } from 'react-bootstrap';
import {
  AiFillFacebook,
  AiFillTwitterCircle,
  AiFillInstagram,
  AiFillPhone,
  AiOutlineMail,
} from 'react-icons/ai';

const Home = () => {
  const [profile, setProfile] = useState([]);

  const fetchProfileData = () => {
    fetch('http://localhost:8000/api/profile/')
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setProfile(data);
      });
  };
  useEffect(() => {
    fetchProfileData();
  }, []);
  return (
    <div id='home'
      style={{
        backgroundColor: '#ffffff',
        paddingTop: '100px',
        paddingBottom: '100px',
      }}
    >
      {profile.map((profil) => (
        <Row key={profil.id}>
          <Container fluid>
            <Row>
              <Col sm={12}>
                <h4 className="">{profil.name}</h4>
                <hr />
                <p>{profil.about_us}</p>
              </Col>
 
            </Row>
          </Container>
        </Row>
      ))}
    </div>
  );
};

export default Home;
