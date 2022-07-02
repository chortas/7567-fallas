import { create } from 'apisauce';

const api = create({
  baseURL: process.env.REACT_APP_BEER_EXPERT_URL,
});

export const getBeerInfo = input => api.get('/beer', input);