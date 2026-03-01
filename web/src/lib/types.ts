export interface GroupCountry {
  name: string;
  ISO: string;
  ISO3: string;
}

export interface GroupMeta {
  gid: string;
  acronym: string;
  classifier: string;
  domains: string[];
  name: string;
  description: string;
  countries: GroupCountry[];
}

export interface CountryCode {
  'NAME.EN': string;
  'ISO_3166_2': string;
  'ISO_3166_3': string;
  'FIPS_GEC': string;
  org_id?: string[];
  org_member?: string[];
}

export interface CountryFact {
  cca3: string;
  flag: string;
  name: { common: string; official: string };
  capital: string[];
  region: string;
  subregion: string;
  area: number;
  population: number;
  borders: string[];
  demonyms?: { eng?: { m: string; f: string } };
  translations: Record<string, { official: string; common: string }>;
  currencies?: Record<string, { name: string; symbol: string }>;
  languages?: Record<string, string>;
}

export interface CountryProfile {
  name: string;
  iso3: string;
  profile: string;
}

export interface IndicatorMeta {
  source: string;
  description: string;
  agg: 'sum' | 'mean' | 'weighted';
  weight_by?: string;
  source_url?: string;
  methodology?: string;
  unit?: string;
  source_db?: string;
}

export interface IndicatorRecord {
  indicator: { id: string; value: string };
  country: { id: string; value: string };
  countryiso3code: string;
  date: string;
  value: number | null;
}

export interface TimeSeries {
  dates: string[];
  values: number[];
}

export interface Story {
  slug: string;
  title: string;
  subtitle?: string;
  group_id: string;
  author: string;
  created: string;
  published: boolean;
  hero_stats?: { value: string; label: string; icon?: string }[];
  sections: StorySection[];
}

export interface StorySection {
  type: string;
  style?: string;
  content?: string;
  code?: string;
  format?: string;
  commentary?: string;
  insight?: string;
  groups?: string[];
  indicators?: { code: string; format: string; label?: string }[];
  number?: number;
  title?: string;
  subtitle?: string;
  icon?: string;
  text?: string;
  source?: string;
  attribution?: string;
  chart_data?: Record<string, { dates: string[]; values: number[]; formatted?: string }>;
}

export interface Quote {
  text: string;
  author: string;
}
