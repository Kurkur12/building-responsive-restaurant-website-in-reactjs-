import React, { useEffect, useState } from 'react';
import { Col, Row, Container } from 'react-bootstrap';
import {
  AiFillFacebook,
  AiFillTwitterCircle,
  AiFillInstagram,
  AiFillPhone,
  AiOutlineMail,
} from 'react-icons/ai';

const Footer = () => {
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
    <div id='footer'
      style={{
        backgroundColor: '#dee2e6',
        paddingTop: '10px',
      }}
    >
      {profile.map((profil) => (
        <Row key={profil.id}>
          <Container fluid>
            <Row>
              <Col sm={12}>
                <h4>Contact Us</h4>
                <hr />
                <p>{profil.address}</p>
                <p>
                  <AiFillPhone size={27} />
                  {profil.phone}
                </p>
                <p>
                  <AiOutlineMail size={27} />
                  {profil.email}
                </p>
              </Col>
              <Col sm={12}>
                <h4>Social Media</h4>
                <hr />
                <p>
                  <AiFillFacebook size={35} />
                  <a href={profil.facebook} target='blank' className="text-black text-decoration-none">
                    Facebook
                  </a>
                </p>
                <p>
                  <AiFillTwitterCircle size={35} />
                  <a href={profil.twitter} target='blank' className="text-black text-decoration-none">
                    Twitter
                  </a>
                </p>
                <p>
                  <AiFillInstagram size={35} />
                  <a href={profil.instagram} target='blank' className="text-black text-decoration-none ">
                    Instagram
                  </a>
                </p>
              </Col>
            </Row>
          </Container>
        </Row>
      ))}
    </div>
  );
};

export default Footer;
