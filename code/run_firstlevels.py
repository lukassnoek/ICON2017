from skbold.exp_model import FsfCrawler

preproc_dir = '/media/lukas/goliath/ICON2017/data_raw'

crawler = FsfCrawler(preproc_dir=preproc_dir, run_idf='wm',
                     template='mvpa', mvpa_type='trial_wise',
                     output_dir=None, subject_idf='pi', event_file_ext='tsv',
                     func_idf='func', prewhiten=False, derivs=False, mat_suffix=None,
                     sort_by_onset=True, n_cores=5)
crawler.crawl()