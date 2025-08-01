from sklearn.metrics.pairwise import cosine_similarity
import torch

def match_resume_to_jd(resume_text, jd_text, model):
    resume_embed = model.encode(resume_text, convert_to_tensor=True)
    jd_embed = model.encode(jd_text, convert_to_tensor=True)
    sim_score = cosine_similarity(
        [resume_embed.cpu().numpy()],
        [jd_embed.cpu().numpy()]
    )[0][0]
    return sim_score
