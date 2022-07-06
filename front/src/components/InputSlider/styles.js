import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  titles: {
    marginTop: '5px',
    textAlign: 'left',
    fontFamily: '"Copse", serif',
    fontWeight: '400',
    fontSize: '15px',
    lineHeight: '14px'
  },
  sliderGrids: {
    marginTop: '15px'
  },
  firstSliderGrid: {
    marginTop: '25px',
  },
  tooltipsText: {
    fontSize: '14px'
  },
  tooltips: {
    marginLeft: '5px'
  }
}));

export default useStyles;
