import './App.css';
import BeerForm from "./components/BeerForm"
import BeerInfo from "./components/BeerInfo"

import {Box, Grid, CircularProgress} from '@mui/material';
import {getBeerInfo} from './services/beerExpertService';
import React, {useState} from 'react';
import useStyles from './styles';
import logo from './img/lupulo.png'

function App() {
    const classes = useStyles();

    const [beerInfo, setBeerInfo] = useState();
    const [loading, setLoading] = useState(false);

    const fetchBeer = async (input) => {
        setLoading(true);
        const response = await getBeerInfo(input)
        if (response.ok) {
            setBeerInfo(response.data)
            console.log(response.data)
        }

        setLoading(false)
    }

    return (
        <Box className="App background">
            <Grid container justifyContent="center">
                <div className="text-near-logo text-next-to-logo">ARG</div>
                <img src={logo} alt="logo" className="logo-img"/>
                <div className="text-near-logo text-next-to-logo">Y22</div>
            </Grid>
            <div className="center logo">MASTER <br/> BREW</div>
            <Grid container justifyContent="center">
                <div className="text-near-logo text-below-logo">COMPANY</div>
            </Grid>
            <div className="center call-to-action-text">
                Definí las características de la cerveza para <br/> conocer más
                sobre su composición y preparación
            </div>

            <Grid container justifyContent="center">
                <BeerForm getBeerInfo={fetchBeer}/>
            </Grid>

            {loading &&
            <Grid container className={classes.gridContainer}>
                <Grid item xs={12} className={classes.gridProgress}>
                    <CircularProgress sx={{color: '#D3A10D'}}/>
                </Grid>
            </Grid>
            }

            {!loading && beerInfo && (
                <Grid container justifyContent="center" style={{marginTop: '30px'}}>
                    <BeerInfo info={beerInfo}/>
                </Grid>
            )}
        </Box>

    );
}

export default App;
