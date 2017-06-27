from skbold.exp_model import FsfCrawler
import os.path as op

base_dir = '/media/lukas/goliath/ICON2017/data_raw'
preproc_dir = op.join(base_dir, 'preproc')
run_idf = 'wm'
template = 'mvpa'
output_dir = op.join(base_dir, 'first_level')
subject_idf = 'pi'
func_idf = 'func'
prewhiten = True
derivs = False
n_cores = 5

fsfc= FsfCrawler(preproc_dir, run_idf, template=template,
                 output_dir=output_dir, subject_idf=subject_idf,
                 func_idf=func_idf, prewhiten=prewhiten, derivs=derivs,
                 n_cores=n_cores)

fsfc.crawl()
