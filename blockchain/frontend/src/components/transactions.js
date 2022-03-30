import React from 'react';
import { Container, Table } from 'react-bootstrap';
import axios from 'axios';

const endpoint = '/blockchain/get_chain/';

export default function Transactions() {
    const [transactions, setTransactions] = React.useState([]);

    React.useState(() => {
        (async () => {
            try {
                const response = await axios.get(endpoint);
                setTransactions(response.data.chain);
            } catch (error) {
                console.log(error);
            };
        })();
    });

    return (
        <Container>
            <h3><b> Transactions </b></h3>
            <p>(Sync to get the latest transactions in the blockchain)</p>
            <Table responsive>
                <thead>
                    <tr>
                        <th>From</th>
                        <th>To</th>
                        <th>Amount (Sudo)</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {transactions.slice(0).reverse().map(transaction =>
                        transaction.transactions.map(t =>
                            <tr key={t}>
                                <td><b style={{ color: '#007bff' }}>0x{t.sender}</b></td>
                                <td><b style={{ color: '#007bff' }}>0x{t.receiver}</b></td>
                                <td><b style={{ color: '#007bff' }}>{parseFloat(t.amount).toFixed(5)} </b></td>
                                <td><b style={{ color: '#007bff' }}>{t.time}</b></td>
                            </tr>
                        ))}
                </tbody>
            </Table>
        </Container>
    );
};