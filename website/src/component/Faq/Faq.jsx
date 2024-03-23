import { Accordion, Row, Col } from 'react-bootstrap';
import React, { useEffect, useState } from 'react';

const Faq = () => {
  const [faq, setFaq] = useState([]);

  const fetchFaqData = () => {
    fetch('http://localhost:8000/api/faq/')
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setFaq(data);
      });
  };

  
  useEffect(() => {
    fetchFaqData();
  }, []);
  return (
    <div className="pb-4" id='faq'>
      <Row lg={2}>
        {faq.map((faq) => {
          return (
            <Col md={4} className="pt-4" key={faq.id}>
              <Accordion defaultActiveKey="0">
                <Accordion.Item eventKey="0">
                  <Accordion.Header>{faq.question}</Accordion.Header>
                  <Accordion.Body>{faq.answer}
                  </Accordion.Body>
                </Accordion.Item>
              </Accordion>
            </Col>
          );
        })}
      </Row>
    </div>
  );
};

export default Faq;
