import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  card: {
    margin: "0 auto"
  },
  buttonsGrid: {
    marginTop: '15px',
    textAlign: 'right',
  },
  titles: {
    marginTop: '5px',
    //textAlign: 'center',
  },
  mobility: {
    marginTop: '5px',
  },
  sliderGrids: {
    marginTop: '15px'
  },
  firstSliderGrid: {
    marginTop: '25px'
  },
  tooltipsText: {
    fontSize: '14px'
  },
  tooltips: {
    marginLeft: '5px'
  },
  accordion: {display: "flex", flexDirection: "column"},
  accordionTitle: { width: '33%', flexShrink: 0 },
  accordionSubtitle: { color: '#0000008a' }
}));

export default useStyles;