import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'font-awesome/css/font-awesome.min.css';
import { Container, Row, Col } from 'react-bootstrap';
import axios from 'axios';

const endpoint = '/blockchain/get_chain/';

export default function Status() {
    const [length, setLength] = React.useState([]);
    const [address, setAddress] = React.useState("");

    React.useEffect(() => {
        (async () => {
            try {
                const response = await axios.get(endpoint);
                setLength(response.data.length);
                setAddress(response.data.chain[1].transactions[0].receiver);
            } catch (error) {
                console.log(error);
            };
        })();
    });

    return (
        <Container>
            <br />
            <Row>
                <Col sm="6">
                    <h5> <div><i className="fa fa-cubes"></i></div> No. of Blocks Mined </h5> <hr />
                    <h5 style={{ color: '#007bff' }}>#<b>{length} </b></h5>
                </Col>
                <Col md="6"> <br />
                    <h5> <div>Node Address (sync <button ><i className="fa fa-refresh"></i></button> )</div></h5> <hr />
                    <h5 style={{ color: '#007bff' }}>0x{address}</h5>
                </Col >
            </Row>
            <br /><br /><br />
        </Container>
    );
};